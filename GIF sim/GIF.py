import imageio.v3 as iio

filenames = ['lammy1.jpg', 'lammy2.jpg', 'lammy3.jpg']
images = []

for file in filenames:
    images.append(iio.imread(file))

iio.imwrite('EduLammy.gif', images, duration=500, loop = 0)