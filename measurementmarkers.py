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
	#mc.player.setPos(0, 0, 0)
	x, y, z = mc.player.getPos()  
	mc.setBlock(x+5, y-1, z+5, 81)
	mc.setBlock(x+5, y-1, z-5, 81)
	mc.setBlock(x-5, y-1, z+5, 81)
	mc.setBlock(x-5, y-1, z-5, 81)
	mc.setBlock(x+5, y-1, z, 48)
	mc.setBlock(x-5, y-1, z, 48)
	mc.setBlock(x, y-1, z+5, 48)
	mc.setBlock(x, y-1, z-5, 48)
	mc.setBlock(x+10, y-1, z, 47)
	mc.setBlock(x-10, y-1, z, 47)
	mc.setBlock(x, y-1, z+10, 47)
	mc.setBlock(x, y-1, z-10, 47)
	mc.setBlock(x+10, y-1, z+10, 41)
	mc.setBlock(x-10, y-1, z-10, 41)
	mc.setBlock(x+10, y-1, z-10, 41)
	mc.setBlock(x-10, y-1, z+10, 41)
	mc.setBlock(x+10, y-1, z+5, 82)
	mc.setBlock(x+10, y-1, z-5, 82)
	mc.setBlock(x-10, y-1, z+5, 82)
	mc.setBlock(x-10, y-1, z-5, 82)
	mc.setBlock(x+5, y-1, z+10, 82)
	mc.setBlock(x+5, y-1, z-10, 82)
	mc.setBlock(x-5, y-1, z+10, 82)
	mc.setBlock(x-5, y-1, z-10, 82)
main()
