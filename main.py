import sys, fitz,os  # import the binding


def pdftojpg(file,filename,zoom):
    fname = filename.replace('.pdf','')    
    if not os.path.exists(fname):
        os.mkdir(fname)

    for page in file:  # iterate through the pages
        # pix = page.getPixmap(alpha = False)  # render page to an image
        # pix.writePNG(F"./{fname}/page-{page.number+1}.png")  # store image as a PNG
        zoom_x = int(zoom)  # horizontal zoom
        zomm_y = int(zoom)  # vertical zoom
        mat = fitz.Matrix(zoom_x, zomm_y)  # zoom factor 2 in each dimension
        pix = page.get_pixmap(matrix = mat)  # use 'mat' instead of the identity matrix
        # pix.writePNG(F"./{fname}/page-{page.number+1}.png")  # store image as a PNG
        pix.writeJPEG(F"./{fname}/page-{page.number+1}.jpg")

if __name__ == "__main__":
    fname = input("输入PDF文件名：")  # get filename from command line
    while True:
        zoom = input("输出尺寸倍数（1-10）：")
        zoom = float(zoom)
        if zoom<=10.0 and zoom>=1.0:
            break
        else:
            print("输出尺寸倍数不符合1-10区间，重新输入。")
    # fname = fname.lower()
    try:
        doc = fitz.open(fname)  # open document
    except IOError as err:
        print(err)
        print('IOError')
    except RuntimeError as err:
        print(err)
        print('RuntimeError')
    else:
        pdftojpg(doc,fname,zoom)
        