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
	mc.setBlocks(x+5, y, z+1, x+5, y+3, z+4, 49)
	mc.setBlocks(x+5, y, z-1, x+5, y+3, z-4, 49)
	mc.setBlocks(x-5, y, z+1, x-5, y+3, z+4, 49)
	mc.setBlocks(x-5, y, z-1, x-5, y+3, z-4, 49)
	mc.setBlocks(x+1, y, z+5, x+4, y+3, z+5, 49)
	mc.setBlocks(x-1, y, z+5, x-4, y+3, z+5, 49)
	mc.setBlocks(x+1, y, z-5, x+4, y+3, z-5, 49)
	mc.setBlocks(x-1, y, z-5, x-4, y+3, z-5, 49)
	mc.setBlocks(x+4, y+3, z-4, x+4, y+3, z+3,114,4)
	mc.setBlocks(x+4, y+3, z+4, x-3, y+3, z+4,114,6)
	mc.setBlocks(x-4, y+3, z+4, x-4, y+3, z-3,114,5)
	mc.setBlocks(x-4, y+3, z-4, x+3, y+3, z-4,114,7)
	mc.setBlocks(x+3, y+4, z-3, x+3, y+4, z+2,114,4)
	mc.setBlocks(x+3, y+4, z+3, x-2, y+4, z+3,114,6)
	mc.setBlocks(x-3, y+4, z+3, x-3, y+4, z-2,114,5)
	mc.setBlocks(x-3, y+4, z-3, x+2, y+4, z-3,114,7)
	mc.setBlocks(x+2, y+5, z-2, x+2, y+5, z+1,114,4)
	mc.setBlocks(x+2, y+5, z+2, x-1, y+5, z+2,114,6)
	mc.setBlocks(x-2, y+5, z+2, x-2, y+5, z-1,114,5)
	mc.setBlocks(x-2, y+5, z-2, x+1, y+5, z-2,114,7)
	mc.setBlocks(x+1, y+6, z-1, x+1, y+6, z,114,4)
	mc.setBlocks(x+1, y+6, z+1, x, y+6, z+1,114,6)
	mc.setBlocks(x-1, y+6, z+1, x-1, y+6, z,114,5)
	mc.setBlocks(x-1, y+6, z-1, x, y+6, z-1,114,7)
	mc.setBlock(x,y+7,z,89)
	mc.setBlocks(x+4, y+4, z-4, x+4, y+4, z+3,114)
	mc.setBlocks(x+4, y+4, z+4, x-3, y+4, z+4,114,2)
	mc.setBlocks(x-4, y+4, z+4, x-4, y+4, z-3,114,1)
	mc.setBlocks(x-4, y+4, z-4, x+3, y+4, z-4,114,3)
	mc.setBlocks(x+3, y+5, z-3, x+3, y+5, z+2,114,)
	mc.setBlocks(x+3, y+5, z+3, x-2, y+5, z+3,114,2)
	mc.setBlocks(x-3, y+5, z+3, x-3, y+5, z-2,114,1)
	mc.setBlocks(x-3, y+5, z-3, x+2, y+5, z-3,114,3)
	mc.setBlocks(x+2, y+6, z-2, x+2, y+6, z+1,114,)
	mc.setBlocks(x+2, y+6, z+2, x-1, y+6, z+2,114,2)
	mc.setBlocks(x-2, y+6, z+2, x-2, y+6, z-1,114,1)
	mc.setBlocks(x-2, y+6, z-2, x+1, y+6, z-2,114,3)
	mc.setBlocks(x+1, y+7, z-1, x+1, y+7, z,114,)
	mc.setBlocks(x+1, y+7, z+1, x, y+7, z+1,114,2)
	mc.setBlocks(x-1, y+7, z+1, x-1, y+7, z,114,1)
	mc.setBlocks(x-1, y+7, z-1, x, y+7, z-1,114,3)

	

main()
