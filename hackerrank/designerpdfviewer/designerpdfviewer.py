
# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    w = sorted(word)
    max =0 

    for i in range(len(word)):
            if h[ord(w[i])-97] > max:
                max = h[ord(w[i])-97]
    return( max * len(w))

if __name__ == '__main__':
   
    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(str(result))

    