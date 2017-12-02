def write(filename):
    file = []
    keep_run = True
    try:
        with open(filename, 'a') as write:
            while keep_run:
                input_text = input("请输入内容：")
                if input_text != '':
                    if input_text != "#":
                        file.append(input_text)
                        write.write(input_text+"\n")
                    elif input_text == "#":
                        for temp in file:
                            print(temp)
                            keep_run = False
                    else:
                        pass
                else:
                    pass
    except:
        print("异常，退出")
    finally:
        pass


if __name__ == "__main__":
    write("cai.txt")