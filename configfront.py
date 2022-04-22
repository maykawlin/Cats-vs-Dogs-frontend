from os.path import join, dirname, abspath
import sys
sys.path.insert(0,join(join(dirname(abspath(__file__)),'ml-backend'),'scripts'))
sys.path.insert(1,join(join(dirname(abspath(__file__)),'ml-backend'),'scripts'))
sys.path.append(join(join(join(dirname(abspath(__file__)),'ml-backend'),'scripts'),'main.py'))

print(sys.path)

#from mainback import model_prediction