import pickle


loaded_model = pickle.load(open('data_prepearing/finalized_model.sav', 'rb'))

result = loaded_model.predict(['BATTERY DOMESTIC BATTERY SIMPLE APARTMENT'])
print(result)
