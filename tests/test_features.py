from pytest_bdd import scenarios

from steps.hello_steps import *
from steps.authentication_steps import *

scenarios("../features")