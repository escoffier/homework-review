"""Crop an original homework photo for manual formula verification (requires Pillow).
Example: python inspect_formula.py INPUT.jpeg --box .08 .52 .49 .64 --output /tmp/formula
Coordinates are fractions of the EXIF-oriented original; source files remain unchanged.
"""
import argparse
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('image',type=Path)
 parser.add_argument('--box',type=float,nargs=4,required=True,metavar=('LEFT','TOP','RIGHT','BOTTOM'))
 parser.add_argument('--output',type=Path,required=True,help='New directory for verification crops')
 args=parser.parse_args()
 left,top,right,bottom=args.box
 if not (0<=left<right<=1 and 0<=top<bottom<=1):parser.error('box must satisfy 0 <= left < right <= 1 and 0 <= top < bottom <= 1')
 im=ImageOps.exif_transpose(Image.open(args.image)).convert('RGB')
 w,h=im.size;crop=im.crop((int(left*w),int(top*h),int(right*w),int(bottom*h)))
 if crop.width==0 or crop.height==0:parser.error('box is too small')
 args.output.mkdir(parents=True,exist_ok=False)
 zoom=crop.resize((crop.width*3,crop.height*3),Image.Resampling.LANCZOS)
 views={'original.png':crop,'zoom-3x.png':zoom,'contrast-3x.png':ImageEnhance.Contrast(ImageOps.grayscale(zoom)).enhance(1.4)}
 for name,view in views.items():
  path=args.output/name;view.save(path);print(path.resolve())
 print('Inspect original and enhanced crops together; enlargement cannot recover missing detail.')

if __name__=='__main__':main()
