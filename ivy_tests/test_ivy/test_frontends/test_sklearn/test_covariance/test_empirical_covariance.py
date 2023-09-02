import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers import handle_frontend_test
from hypothesis import strategies as st

@handle_frontend_test(
    fn_tree="sklearn.covariance.empirical_covariance",
    dtype_and_x=helpers.dtype_and_values(
        available_dtypes= helpers.get_dtypes("valid"),
        min_num_dims=1,
        max_num_dims=2,
        min_dim_size=1,
        max_dim_size=3,
    ),
    assume_centered = st.booleans()
)
def test_sklearn_empirical_covariance(
    dtype_and_x,
    on_device,
    assume_centered,
    fn_tree,
    frontend,
    test_flags,
    backend_fw,
):
    dtypes, x = dtype_and_x
    helpers.test_frontend_function(
        input_dtypes=dtypes,
        backend_to_test=backend_fw,
        test_flags=test_flags,
        fn_tree=fn_tree,
        frontend=frontend,
        on_device=on_device,
        X=x[0],
        assume_centered=assume_centered
    )