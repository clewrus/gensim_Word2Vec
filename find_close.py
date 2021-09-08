from gensim.models import Word2Vec
import pymorphy2
import sys

morph = pymorphy2.MorphAnalyzer( lang='uk' )
model = Word2Vec.load( sys.argv[1] )
normal_word = morph.parse( sys.argv[2] )[0].normal_form
close_words = model.wv.most_similar( normal_word )
print( '\n'.join( map(str, close_words) ) )