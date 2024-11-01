# third party libraries i.e. Packages
# to search the third party packages and get the we can visit pypi.org
# can download it too and we can easily install using the py manager 'pip'
# e.g. - pip install 'package_name'
import cowsay # i just installed the cowsay ok it creates a cool text art with that though cloud you know it lol
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])

print("\n")

cowsay.trex("hello dawg")