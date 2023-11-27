import os
from tqdm import tqdm
import __main__


def yoloformat(FOLDER_LOC, FILE_NAME):
    os.chdir(FOLDER_LOC)

    files_len = len(os.listdir("."))

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


if __name__ == '__main__':
    yoloformat('eanalyzer/labels', 'euglena-m1')
    print('Done')
