from os import getcwd

class Utils:
	@staticmethod
	def checkout(b: bool, w: str): 
		if b: print(f'Reconheceu: {w}')
		else: print(f'Não reconheceu: {w}')
  
	@staticmethod
	def readFile(file_name: str):
		f, res, dir = None, '', getcwd() + '\\'
  
		try:
			f = open(dir + file_name, 'r')
			res = f.read()
   
		except FileNotFoundError:
			print(f'"{file_name}" doesn\'t exist')
   
		finally:
			f.close()
   
		return res

	@staticmethod
	def writeFile(file_name: str, content: str): 
		f, dir = None, getcwd() + '\\'
  
		try:
			f = open(dir + file_name, 'w')
			f.write(content)
   
		except Exception as e:
			print(f'Can\'t write in "{file_name}"')
   
		finally:
			f.close()