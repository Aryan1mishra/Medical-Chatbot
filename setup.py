from setuptools import setup, find_packages

setup(
    name='medical_chatbot',
    version='0.1',
    packages=find_packages(),
    author='Aryan Mishra',
    install_requires=[
        'langchain==0.3.26',
        'flask==3.1.1',
        'sentence-transformers==4.1.0',
        'pypdf==5.6.1',
        'python-dotenv==1.1.0',
        'langchain-pinecone==0.2.8',
        'langchain-openai==0.3.24',
        'langchain-community==0.3.26'
        
    ]
)