from image import Image
import matplotlib.pyplot as plt

im=Image()
im.load_from_pgm("./chat.pgm")
#print(im.matrix)

# im.histogram_equalizer().save_to_pgm("egalisé")

# im.etire().save_to_pgm("etiresamx")
# im.decalage(100).save_to_pgm("100")
# im.decalage(30).etire().save_to_pgm("30etire")

# im.contrast_morceau(50,50,80,150).save_to_pgm("chatclaire")

# plt.plot(range(0,256),im.contrast_morceau(50,50,80,150).histogram())
# plt.xlabel('Grey levels')
# plt.ylabel('Occurance')
# plt.title('Histogram')
# plt.show()

# b=im.bruit()
# b.save_to_pgm("bruit")
# b.average(3).save_to_pgm("moy3X3")
# b.median(3).save_to_pgm("median3X3")
# b.average(5).save_to_pgm("moy5X5")
# b.median(5).save_to_pgm("median5X5")
# im.passeHaut().save_to_pgm("passeHaut")
# print("SNR average 3X3 ",im.variance(b.average(3)))
# print("SNR average 5X5 ",im.variance(b.average(5)))
# print("SNR median 3X3 ",im.variance(b.median(3)))
# print("SNR median 5X5 ",im.variance(b.median(5)))
# print("SNR passe Haut ",im.variance(b.passeHaut()))


im.load_from_ppm("./peppers.ppm",100,80,150)
im.save_to_pgm("seuil")
im.load_from_ppmET("./peppers.ppm",100,50,100)
im.save_to_pgm("seuilET")
im.load_from_ppmOU("./peppers.ppm",110,50,100)
im.save_to_pgm("seuilOU")
# print(im.matrix)




