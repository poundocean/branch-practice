def buzz():
    for i in range(1,15+1):
        if i%5==0:
            print('buzz')
        else:
            print(f'{i}')


if __name__=='__main__':
    buzz()
