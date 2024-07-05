import os
from utils.image_segmenter import segment_images

def main(input_folder, output_folder):
    segment_images(input_folder, output_folder)

if __name__ == "__main__":
    input_base_folder = '/media/minigo/Disco/modelado3d/santiago/codigos/image_generator_2/data/images'
    output_base_folder = '/media/minigo/Disco/modelado3d/santiago/codigos/image_generator_2/data/segment_images'
    
    for class_folder in os.listdir(input_base_folder):
        input_folder = os.path.join(input_base_folder, class_folder)
        output_folder = os.path.join(output_base_folder, class_folder)
        main(input_folder, output_folder)
