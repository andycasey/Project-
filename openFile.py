
from astropy.table import Table

galah = Table.read("GALAH_DR2.1_catalog.fits")

use_for_training = (galah["cannon_flag"] == 0) \
		 * (galah["logg"] > 4) \
		 * (galah["snr_c1"] > 100) \
		 * ((galah["vsini"] < 20) | (galah["vsini"] == 0)) \

print("There are {0} stars that met criteria".format(sum(use_for_training)))
