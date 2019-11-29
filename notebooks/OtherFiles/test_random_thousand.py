# imports here if necessary

# lets create some tests!
def test_defined_range():
    # create a test that throws an appropriate exception if upper_bound is less than lower_bound


def test_length():
    # make sure that the function returns the right number of values (we wanted 1000

def test_boundaries():
    # create a test that checks that every value of the return is within an expected range. Test this 
    # for a few different ranges. (Hint: you may need to make another method to help you do this)

def test_uniform_distribution1():
    # create a test that will show that the median value is roughly the value that is halfway between
    # the lower and upper boundary.

def test_uniform_distribution2():
    # create a test that will show that the mean value is roughly the median value. This can be done 
    # either with nose.tools.assert_almost_equal or by checking that the mean is within a small range
    # centered on the median.

def test_return_type():
    # create a test that assures the return value type is a numpy array


# The next test is very challenging, requiring you to look into matplotlib documentation
# As a result, this next test is optional
def test_uniform_distribution3():
    # create a histogram plot of the random values. Make sure that the smallest histogram bin is
    # roughly the same size of the largest histogram bin. Choose a bin count large enough to show
    # a reasonable amount of detail, but no so many that the bins look sparse.