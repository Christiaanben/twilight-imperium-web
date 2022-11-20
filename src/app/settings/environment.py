import os.path
import sys
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

os.environ['test'] = str('test' in sys.argv or 'test_coverage' in sys.argv)


def load_environment():
    env = environ.Env()
    if env.str('SECRET_KEY', default='') == '':
        env_file = env.str('ENV', default='local')
        if not env_file.endswith('.env'):
            env_file += '.env'
        env_file = os.path.join(BASE_DIR.parent, 'environments', env_file)
        print(f'Loading environment from: {env_file}')
        env.read_env(env_file)
    return env


env = load_environment()
