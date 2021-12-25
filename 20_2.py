with open('tests/20_2.input', 'r') as inp:
    alg, img = [x for x in inp.read()[:-1].split('\n\n')]
    img = img.split('\n')
    enh = 50
    exp = ''.join('.' for i in range(enh + 1))
    tmp_img = [exp + x + exp for x in img]
    e = [''.join(['.' for x in tmp_img[0]]) for i in range(enh + 1)]
    tmp_img = e + tmp_img + e

    out_img = [['.' for x in line] for line in tmp_img]

    for t in range(enh):
        # i == 0: stands for inf
        for j in range(len(tmp_img[0])):
            val = tmp_img[0][0]
            val = val.replace('.', '0')
            val = val.replace('#', '1')
            idx = int(val, 2)
            out_img[0][j] = alg[idx]
        # i == len - 1: stands for inf
        for j in range(len(tmp_img[-1])):
            val = tmp_img[-1][0]
            val = val.replace('.', '0')
            val = val.replace('#', '1')
            idx = int(val, 2)
            out_img[-1][j] = alg[idx]
        # j == 0: stands for inf
        for i in range(len(tmp_img)):
            val = tmp_img[0][0]
            val = val.replace('.', '0')
            val = val.replace('#', '1')
            idx = int(val, 2)
            out_img[i][0] = alg[idx]
        # j == len - 1: stands for inf
        for i in range(len(tmp_img)):
            val = tmp_img[0][-1]
            val = val.replace('.', '0')
            val = val.replace('#', '1')
            idx = int(val, 2)
            out_img[i][-1] = alg[idx]
        # all other
        for i in range(1, len(tmp_img) - 1):
            for j in range(1, len(tmp_img[i]) - 1):
                val = tmp_img[i - 1][j - 1:j + 2] + \
                      tmp_img[i][j - 1:j + 2] + \
                      tmp_img[i + 1][j - 1:j + 2]
                val = val.replace('.', '0')
                val = val.replace('#', '1')
                idx = int(val, 2)
                out_img[i][j] = alg[idx]

        tmp_img = [''.join(x) for x in out_img]

    print(sum(1 for line in out_img for x in line if x == '#'))