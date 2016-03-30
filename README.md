# validata
### Continuous integration for your data

We do continuous integration on code. Why not data?
Validata is a small package to run basic sanity checks on your data.
I haven't found anything that aggregates all of these checks and tricks in one place.

There is only one method which is exposed, `check(data,labels)` (optionally taking data or labels).
If any data check fails, it throws a well-named error, as well as hints for how you might fix the problem -- data covariance matrix ill-conditioned? Try whitening.

Initially, this will be a Python/NumPy only package running basic checks, but hopefully it becomes a resource of data sanity and sanitation checks.
Still very much a work in progress.


Examples (some implemented, some not) include:

 - If your labels are one-hot, are you using all slots?
 - Is the covariance matrix of your data ill-conditioned?
 - Do you have any constant variables?
 - Can you train a classifier to distinguish train and test data, using whether they are in train or test as a label? Indicates different data distributions.
 - If you're using integer labels, are the unique labels contiguous?
 - Do you have just one unique label?
 - Is the data under different labels statistically separable?
 - If you have an old dataset and a new dataset (or two halves of the same dataset), is the distribution of each dimension stationary? Check for divergence with a KS test.
 - What else? I end up applying these tricks in a very ad hoc fashion, whenever a subtle bug pops up, and not rigorously before each project I tackle. I'd like to stuff all these tricks in one place, and run them like a unit test, or a continuous integration test, on data that I start working with.