import os


if __name__ == "__main__":
    print("In Main")
    this_dir = os.path.dirname(__file__)
    root_dir = os.path.dirname(this_dir)
    weights_file = os.path.join(root_dir, "assets", f'{"yolov7"}.pt')

    print(f"this_dir: {this_dir}")
    print(f"thisroot_dir_dir: {root_dir}")
    print(f"weights_file: {weights_file}")