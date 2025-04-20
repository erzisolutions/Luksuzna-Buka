
from setuptools import setup, find_packages

setup(
    name='luksuzna-buka',
    version='1.0.0',
    description='AI-powered mastering & BCS audio processing suite',
    author='Erzi',
    author_email='kontakt@luksuznabuka.ai',
    url='https://github.com/erzi-ai/luksuzna-buka',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'torch',
        'librosa',
        'pydub',
        'pedalboard',
        'transformers',
        'pyannote.audio',
        'diffusers',
        'soundfile',
        'streamlit',
        'flask',
        'ray',
        'mlflow',
        'onnxruntime',
        'gradio'
    ],
    entry_points={
        'console_scripts': [
            'luksuzna-buka = launcher:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
)
