import os
from tqdm import tqdm
import __main__


def cvtyoloformat_old(FOLDER_LOC, FILE_NAME, max_frame):

    os.chdir(FOLDER_LOC)
    if max_frame is None:
        files_len = len(os.listdir("."))
    else:
        files_len = max_frame

    last_list = []
    with open(f'{FILE_NAME}_{files_len - 1}.txt', 'r+') as f:
        for line in f:
            line_list = line.split()
            line_list = [float(line_ctx) for line_ctx in line_list]
            last_list.append(line_list[-1])
            max_id = int(max(last_list))

    for h in tqdm(range(max_id)):
        tracking_result = []
        for i in range(files_len - 1):
            txt_2_list = []
            with open(f'{FILE_NAME}_{str(i+1)}.txt', 'r+') as f:
                for line in f:
                    line_list = line.split()
                    line_list = [float(line_ctx) for line_ctx in line_list]
                    txt_2_list.append(line_list)
            for j in range(len(txt_2_list)):
                if (txt_2_list[j][len(txt_2_list[j])-1] == float(h) + 1.0):
                    tracking_result.append(txt_2_list[j])

        with open(f'./output/{FILE_NAME}_{h+1}.txt', 'w') as f:
            for line in tracking_result:
                f.write(str(line))
                f.write('\n')


def cvtyoloformat(FOLDER_LOC, FILE_NAME, max_frame=None):
    os.chdir(FOLDER_LOC)
    os.mkdir('output')
    if max_frame is None:
        files_len = len(os.listdir("."))
    else:
        files_len = max_frame

    for l in tqdm(range(files_len)):
        if (os.path.isfile(f'{FILE_NAME}_{l+1}.txt') == True):
            with open(f'{FILE_NAME}_{l+1}.txt', 'r') as f:
                for line in f:
                    line_list = line.split()
                    line_list = [float(line_ctx) for line_ctx in line_list]
                    if (len(line_list) > 10):
                        with open(f'./output/{FILE_NAME}_{line_list[-1]}.txt', 'a') as f:
                            f.write(str(line))
        else:
            continue


if __name__ == '__main__':
    cvtyoloformat('eanalyzer/labels/', 'IMG_0038')
    print('Done')
