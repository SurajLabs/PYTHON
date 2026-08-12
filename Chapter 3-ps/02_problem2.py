letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|> '''
print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "19 october 2025"))