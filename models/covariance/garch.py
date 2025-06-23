import warnings
from arch.univariate.base import DataScaleWarning
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", DataScaleWarning)
warnings.filterwarnings("ignore", ConvergenceWarning)

class GARCHCovarianceModel(BaseEstimator):
    def __init__(self, p=1, q=1, scale=100):
        self.p, self.q, self.scale = p, q, scale
        self._cov = None

    def fit(self, X, y=None):
        X = np.asarray(X) * self.scale             # <-- manual scaling
        n_obs, n_ser = X.shape
        cond_vol = np.zeros((n_obs, n_ser))
        std_resid = np.zeros_like(cond_vol)

        for i in range(n_ser):
            g = arch_model(
                X[:, i],
                mean="zero", vol="GARCH", p=self.p, q=self.q,
                dist="normal", rescale=False        # <-- disable auto‐rescale
            )
            res = g.fit(disp="off", options={"maxiter": 200})
            vol = res.conditional_volatility / self.scale  # <-- undo scale
            cond_vol[:, i] = vol
            std_resid[:, i] = res.resid / res.conditional_volatility

        corr = np.corrcoef(std_resid.T)
        last_sigma = cond_vol[-1, :]
        D = np.diag(last_sigma)
        self._cov = D @ corr @ D
        return self

    def predict(self, X):
        """
        Returns the same covariance matrix for each sample in X.
        """
        m = np.asarray(X).shape[0]
        return np.repeat(self._cov[np.newaxis, :, :], m, axis=0)

    @property
    def covariance_(self):
        """Latest estimated covariance matrix."""
        return self._cov
