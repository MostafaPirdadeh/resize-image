import os
from PIL import Image

def resize_images(image_folder, output_folder, resampling_filter=Image.BILINEAR):
  
  for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
      # خواندن تصویر
      image = Image.open(os.path.join(image_folder, filename))

      # تغییر اندازه تصویر
      resized_image = image.resize((512, 512), resampling_filter)

      # ذخیره تصویر تغییر اندازه داده شده
      resized_image.save(os.path.join(output_folder, filename))

if __name__ == "__main__":
  image_folder = r"C:\Users\negin\Desktop\C-VEA\train\healthy"  
  output_folder = "train/healthy" 
  resampling_filter = Image.BILINEAR 

  resize_images(image_folder, output_folder, resampling_filter)
