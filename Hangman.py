import random as rd

menu = True
run = False
wins = 0
losses = 0
choices = ["1", "2", "3", "4"]

words_dict = {
    1: [
        "elephant", "giraffe", "penguin", "dolphin", "kangaroo",
        "butterfly", "hummingbird", "rhinoceros", "alligator", "ostrich",
        "flamingo", "hippopotamus", "crocodile", "chimpanzee", "gorilla",
        "meerkat", "peacock", "platypus", "salamander", "tarantula",
        "octopus", "starfish", "hedgehog", "armadillo", "beetle",
        "triceratops", "pterodactyl", "saber-toothed", "mammoth", "dodo",
        "unicorn", "dragon", "phoenix", "griffin", "chimera",
        "basilisk", "hydra", "pegasus", "minotaur", "kraken",
        "yeti", "centaur", "mermaid", "banshee", "wyvern",
        "cerberus", "leviathan", "sphinx", "gorgon", "wendigo",
        "narwhal", "quagga", "moa", "thylacine", "megalodon",
        "velociraptor", "ankylosaurus", "pterosaur", "ichthyosaurus", "plesiosaur",
        "pachycephalosaurus", "stegosaurus", "brachiosaurus", "allosaurus", "mosasaurus",
        "direwolf", "glyptodon", "terrorbird", "mastodon", "megatherium",
        "quagga", "aurochs", "woollyrhinoceros", "saber-toothtiger", "ornithomimus",
        "gargoyle", "hippogriff", "manticore", "succubus", "kitsune",
        "naga", "fenrir", "sasquatch", "chupacabra", "troll",
        "orc", "imp", "kelpie", "faun", "cyclops",
        "satyr", "harpy", "selkie", "basilisk", "roc",
        "golem", "zouwu", "jiangshi", "kitsune", "taniwha"
    ],
    2: [
        "harrypotter", "hermionegranger", "ronweasley", "albusdumbledore", "severussnape",
        "voldemort", "dracomalfoy", "siriusblack", "remuslupin", "minervamcgonagall",
        "ginnyweasley", "fredweasley", "georgeweasley", "arthurweasley", "mollyweasley",
        "nevillelongbottom", "lunalovegood", "chochang", "cedricdiggory", "hagrid",
        "alastormoody", "bellatrixlestrange", "peterpettigrew", "luciusmalfoy", "narcissamalfoy",
        "fleurdelacour", "kingsleyshacklebolt", "ninfadora tonks", "corneliusfudge", "argusfilch",
        "gilderoylockhart", "horaceslughorn", "madamepomfrey", "bartycrouch", "bartycrouchjr",
        "seamusfinnigan", "deanthomas", "oliverwood", "percyweasley", "billweasley",
        "charlieweasley", "lavenderbrown", "parvatipatil", "padmapatil", "angelinajohnson",
        "katiebell", "mariettaconfiscated", "penelopeclearwater", "ernieprang", "tomriddle",
        "gregorygoyle", "vincentcrabbe", "doloresumbridge", "sybilltrelawney", "moaningmyrtle",
        "nearlyheadlessnick", "fatfriar", "greyfriar", "peevesthepoltergeist", "firenze",
        "griphook", "bogrod", "gornuk", "dob", "kreacher",
        "winky", "hokey", "yaxley", "scabior", "fenrirgreyback",
        "floreanfortescue", "garrickollivander", "elphiasdoge", "mundungusfletcher", "arabelladiggory",
        "abernathydigory", "rubeushagrid", "madamehooch", "pomonavspro", "rolandamarchbanks",
        "octaviuspepple", "quenellogorum", "zacharias", "yaxley", "teddyremuslupin",
        "tedtonks", "andromedatonks", "katiebell", "aliciaspinnet", "leestrange",
        "basilisk", "fang", "buckbeak", "aragog", "norbert",
        "trevor", "hedwig", "scabbers", "crookshanks", "errol"
    ],
    3: [
        "python", "javascript", "java", "csharp", "ruby",
        "php", "swift", "kotlin", "typescript", "go",
        "rust", "perl", "objectivec", "scala", "haskell",
        "elixir", "erlang", "lua", "dart", "matlab",
        "r", "c", "cplusplus", "shell", "powershell",
        "visualbasic", "assembly", "fsharp", "fortran", "cobol",
        "julia", "groovy", "bash", "vhdl", "verilog",
        "prolog", "lisp", "scheme", "smalltalk", "elm",
        "crystal", "nim", "ocaml", "racket", "tcl",
        "ada", "abap", "awk", "cobol", "delphi",
        "vbscript", "sas", "plsql", "labview", "scratch",
        "processing", "coffeescript", "clojure", "postscript", "eiffel",
        "actionscript", "coldfusion", "pascal", "simula", "logo",
        "d", "hack", "vala", "zig", "rexx",
        "red", "mercury", "terraform", "ansible", "puppet",
        "chef", "react", "vue", "angular", "ember",
        "backbone", "svelte", "django", "flask", "spring",
        "laravel", "rails", "express", "nextjs", "nestjs",
        "fastapi", "symfony", "struts", "grails", "bottle",
        "pyramid", "photon", "sinatra", "phoenix", "flutter"
    ]
}

stick_figure_dict = {
    0: """
          


    """,
    1: """
     0      
        
        
        """,
    2: """
     0
     |
     
        """,
    3: """
     0
    /|

    """,
    4: """
     0
    /|\\
    
    """,
    5: """
     0
    /|\\
    /
    """,
    6: """
     0 <You lose!
    /|\\
    / \\
    """,
}

while menu:
    print("""
    ====HANGMAN====
    
    1. Animals
    2. Harry Potter
    3. Programming
    4. Quit
    
    """)
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    choice = input(">>")

    if choice in choices:
        run = True
        guessed_wrong_amount = 0
        guessed_letters = []
        answer = rd.choice(words_dict[int(choice)])
        word_tiles = ["_"] * len(answer)

        while run:
            print(stick_figure_dict[guessed_wrong_amount])
            print(" ".join(word_tiles))
            print(f"Guessed: {', '.join(guessed_letters)}")
            guess = input("Guess a letter: ")

            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue

            guessed_letters.append(guess)

            if guess in answer:
                for i, letter in enumerate(answer):
                    if letter == guess:
                        word_tiles[i] = guess

            else:
                guessed_wrong_amount += 1

            if guessed_wrong_amount == 6:
                print(stick_figure_dict[guessed_wrong_amount])
                print(f"The answer was {answer}! You big silly!")
                losses += 1
                run = False
                break

            if "_" not in word_tiles:
                print("Congratulations! You guessed the word:", "".join(word_tiles))
                wins += 1
                break

    elif choice == '4':
        print("Thank you for playing!")
        menu = False
