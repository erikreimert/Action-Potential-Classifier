import h5py

def main():

    f = h5py.File('Long-term-hc15/2014_12_01_8963_0001.h5', 'r')
    print(list(f.keys()))
    dset = f['Data']
    print(dset.keys())
    print(dset.items())
    print('\n\n')

    a = h5py.File('Long-term-hc15/2014_12_03_8963_0002.h5', 'r')
    print(list(a.keys()))
    dset2 = a['Data']
    print(dset2.keys())
    print(dset2.items())
    print('\n\n')

    f = h5py.File('Long-term-hc15/2014_12_05_8963_0003.h5', 'r')
    print(list(f.keys()))
    dset = f['Data']
    print(dset.keys())
    print(dset.items())
    print('\n\n')


    f = h5py.File('Long-term-hc15/2014_12_07_8963_0004.h5', 'r')
    print(list(f.keys()))
    dset = f['Data']
    print(dset.keys())
    print(dset.items())
    print('\n\n')

    f = h5py.File('Long-term-hc15/2014_12_10_8963_0005.h5', 'r')
    print(list(f.keys()))
    dset = f['Data']
    print(dset.keys())
    print(dset.items())
    print('\n\n')

    f = h5py.File('Long-term-hc15/2014_12_11_8963_0006.h5', 'r')
    print(list(f.keys()))
    dset = f['Data']
    print(dset.keys())
    print(dset.items())
    print('\n\n')

    f = h5py.File('Long-term-hc15/2014_12_16_8963_0007.h5', 'r')
    print(list(f.keys()))
    dset = f['Data']
    print(dset.keys())
    print(dset.items())
    print('\n\n')



if __name__ == '__main__':
    main()
