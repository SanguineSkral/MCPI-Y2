from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init(): 
	# change 192.168.1.13 to 127.0.0.1 or your ip
	mc = Minecraft.create("127.0.0.1", 4711)
	x, y, z = mc.player.getPos()  
	return mc

#main  
def main():
	mc = init()
	x, y, z = mc.player.getPos()  
	mc.setBlock(x+2, y, z, 114, 5)
	mc.setBlock(x+2, y, z+1, 114, 7)
	
	

main()
