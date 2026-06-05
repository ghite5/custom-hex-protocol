import sys

def render_chp_terminal(filename):
    try:
        with open(filename, "r") as file:
            lines = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return

    name = lines[0].split("NAME:")[1].strip()
    author = lines[1].split("AUTHOR:")[1].strip()
    date = lines[2].split("DATE:")[1].strip()
    print("-" * 34)
    print(f"\033[1mFile:\033[0m {filename} | \033[1mTitle:\033[0m {name}")
    print(f"\033[1mArtist:\033[0m {author} | \033[1mDate:\033[0m {date}")
    print("-" * 34)

    for line in lines[3:]:
        row_pixels = line.split()
        for color_string in row_pixels:
            color_id = int(color_string)
            print(f"\033[48;5;{color_id}m  \033[0m", end="")
        print() 
        
    print("-" * 34)

if __name__ == "__main__":
    target_file = sys.argv[1] if len(sys.argv) > 1 else "artwork.chp"
    render_chp_terminal(target_file)
