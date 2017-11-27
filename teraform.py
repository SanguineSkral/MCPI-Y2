from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init(): 
	# change 192.168.1.13 to 127.0.0.1 or your ip
	mc = Minecraft.create("10.183.13.13", 4711)
	x, y, z = mc.player.getPos()  
	return mc

#main  
def main():
	mc = init()
	#mc.player.setPos(0, 0, 0)
	x, y, z = mc.player.getPos()  
	mc.setBlocks(x-50, y+30, z-50, x+50, y+30, z+50, 8)
	mc.setBlocks(x-10, y, z-10,x+10, y+10, z+10, 0)
	mc.setBlocks(x-10, y-1, z-10,x+10, y-1, z+10, 246)
	mc.setBlock(x, y-1, z, 247)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
main()
