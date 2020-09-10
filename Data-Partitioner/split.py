import h5py

def main():

    f = h5py.File('2014_12_01_8963_0001.h5', 'r')
    print(list(f.keys()))
    print(f.shape)


if __name__ == '__main__':
    main()
