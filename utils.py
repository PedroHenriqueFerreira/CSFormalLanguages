class Utils:
	@staticmethod
	def checkout(b: bool, w: str): 
		if b: print(f'Reconheceu: {w}')
		else: print(f'Não reconheceu: {w}')
  
	@staticmethod
	def readFile(file_name: str):
		f, res = None, ''
  
		try:
			f = open(file_name, 'r', encoding='UTF-8')
			res = f.read()
   
		except FileNotFoundError:
			print(f'"{file_name}" doesn\'t exist')
   
		finally:
			f.close()
   
		return res

	@staticmethod
	def writeFile(file_name: str, content: str): 
		f = None
  
		try:
			f = open(file_name, 'w', encoding='UTF-8')
			f.write(content)
   
		except Exception as e:
			print(f'Can\'t write in "{file_name}"')
   
		finally:
			f.close()