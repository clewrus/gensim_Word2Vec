from gensim.models import Word2Vec
import pymorphy2
import sys

dataset_name = sys.argv[1]
target_word = sys.argv[2]

# getting normal form of the word
morph = pymorphy2.MorphAnalyzer( lang='uk' )
normal_word = morph.parse( target_word )[0].normal_form

# loading model
model = Word2Vec.load( dataset_name )

# getting most similar words
close_words = model.wv.most_similar( normal_word )

print( target_word )
print( '\n'.join( map(str, close_words) ) )
