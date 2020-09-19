from PIL import Image
import os
import traceback

def main():
    try:
        print("Welcome...starting to join pictures...")
        print("--------------------------------------")
        print("Before you start, make sure photos are stored in folder named \"images\"!")
        a = input(">>> Yes, I'm aware of that. ")
        # input()
        print("--------------------------------------")
        horizontal_join("./images/")
    except Exception as e:
        print(traceback.format_exc())

def horizontal_join(Dir: str):
    print("---> join mode: [horizontal]")
    image_list = os.listdir(Dir)
    print("Found", str(len(image_list)), "files:", image_list)
    print("--------------------------------------")
    test_img = Image.open(Dir+image_list[0])
    total_size = (test_img.size[0] * len(image_list), test_img.size[1])
    print(total_size)
    target = Image.new("RGB", total_size)
    a, b = 0, 0
    iter_x = test_img.size[0]
    for img_name in image_list:
        print("-> joining:", Dir+img_name)
        img = Image.open(Dir+img_name)
        target.paste(img, (a, b))
        a += iter_x
    target.save("./result.jpg")    
    print("--------------------------------------")
    print("Showing results...")
    target.show()
    print("--------------------------------------")
    print("Finished. \"result.jpg\" is save in current folder. Goodbye~~~")
    




if __name__ == '__main__':
    main()