#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-crul
Version  : 0.7.0
Release  : 11
URL      : https://cran.r-project.org/src/contrib/crul_0.7.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/crul_0.7.0.tar.gz
Summary  : HTTP Client
Group    : Development/Tools
License  : MIT
BuildRequires : R-curl
BuildRequires : R-httpcode
BuildRequires : R-urltools
BuildRequires : buildreq-R

%description
crul
====
[![Project Status: Active - The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Build Status](https://travis-ci.org/ropensci/crul.svg?branch=master)](https://travis-ci.org/ropensci/crul)
[![codecov](https://codecov.io/gh/ropensci/crul/branch/master/graph/badge.svg)](https://codecov.io/gh/ropensci/crul)
[![cran checks](https://cranchecks.info/badges/worst/crul)](https://cranchecks.info/pkgs/crul)
[![rstudio mirror downloads](http://cranlogs.r-pkg.org/badges/crul)](https://github.com/metacran/cranlogs.app)
[![cran version](https://www.r-pkg.org/badges/version/crul)](https://cran.r-project.org/package=crul)

%prep
%setup -q -c -n crul

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552731519

%install
export SOURCE_DATE_EPOCH=1552731519
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library crul
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library crul
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library crul
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  crul || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/crul/DESCRIPTION
/usr/lib64/R/library/crul/INDEX
/usr/lib64/R/library/crul/LICENSE
/usr/lib64/R/library/crul/Meta/Rd.rds
/usr/lib64/R/library/crul/Meta/features.rds
/usr/lib64/R/library/crul/Meta/hsearch.rds
/usr/lib64/R/library/crul/Meta/links.rds
/usr/lib64/R/library/crul/Meta/nsInfo.rds
/usr/lib64/R/library/crul/Meta/package.rds
/usr/lib64/R/library/crul/Meta/vignette.rds
/usr/lib64/R/library/crul/NAMESPACE
/usr/lib64/R/library/crul/NEWS.md
/usr/lib64/R/library/crul/R/crul
/usr/lib64/R/library/crul/R/crul.rdb
/usr/lib64/R/library/crul/R/crul.rdx
/usr/lib64/R/library/crul/doc/async.Rmd
/usr/lib64/R/library/crul/doc/async.html
/usr/lib64/R/library/crul/doc/best-practices-api-packages.R
/usr/lib64/R/library/crul/doc/best-practices-api-packages.Rmd
/usr/lib64/R/library/crul/doc/best-practices-api-packages.html
/usr/lib64/R/library/crul/doc/crul_vignette.Rmd
/usr/lib64/R/library/crul/doc/crul_vignette.html
/usr/lib64/R/library/crul/doc/curl-options.Rmd
/usr/lib64/R/library/crul/doc/curl-options.html
/usr/lib64/R/library/crul/doc/how-to-use-crul.Rmd
/usr/lib64/R/library/crul/doc/how-to-use-crul.html
/usr/lib64/R/library/crul/doc/index.html
/usr/lib64/R/library/crul/help/AnIndex
/usr/lib64/R/library/crul/help/aliases.rds
/usr/lib64/R/library/crul/help/crul.rdb
/usr/lib64/R/library/crul/help/crul.rdx
/usr/lib64/R/library/crul/help/paths.rds
/usr/lib64/R/library/crul/html/00Index.html
/usr/lib64/R/library/crul/html/R.css
/usr/lib64/R/library/crul/tests/test-all.R
/usr/lib64/R/library/crul/tests/testthat/helper-crul.R
/usr/lib64/R/library/crul/tests/testthat/test-async.R
/usr/lib64/R/library/crul/tests/testthat/test-asyncvaried.R
/usr/lib64/R/library/crul/tests/testthat/test-auth.R
/usr/lib64/R/library/crul/tests/testthat/test-client-delete.R
/usr/lib64/R/library/crul/tests/testthat/test-client-get.R
/usr/lib64/R/library/crul/tests/testthat/test-client-head.R
/usr/lib64/R/library/crul/tests/testthat/test-client-patch.R
/usr/lib64/R/library/crul/tests/testthat/test-client-post.R
/usr/lib64/R/library/crul/tests/testthat/test-client-put.R
/usr/lib64/R/library/crul/tests/testthat/test-client-query.R
/usr/lib64/R/library/crul/tests/testthat/test-client-status.R
/usr/lib64/R/library/crul/tests/testthat/test-client-verb.R
/usr/lib64/R/library/crul/tests/testthat/test-client.R
/usr/lib64/R/library/crul/tests/testthat/test-handle.R
/usr/lib64/R/library/crul/tests/testthat/test-headers.R
/usr/lib64/R/library/crul/tests/testthat/test-mocking.R
/usr/lib64/R/library/crul/tests/testthat/test-ok.R
/usr/lib64/R/library/crul/tests/testthat/test-paginator.R
/usr/lib64/R/library/crul/tests/testthat/test-paths.R
/usr/lib64/R/library/crul/tests/testthat/test-proxies.R
/usr/lib64/R/library/crul/tests/testthat/test-request.R
/usr/lib64/R/library/crul/tests/testthat/test-response.R
/usr/lib64/R/library/crul/tests/testthat/test-retry.R
/usr/lib64/R/library/crul/tests/testthat/test-set.R
/usr/lib64/R/library/crul/tests/testthat/test-url_build_parse.R
/usr/lib64/R/library/crul/tests/testthat/test-url_fetch.R
/usr/lib64/R/library/crul/tests/testthat/test-user-agent.R
/usr/lib64/R/library/crul/tests/testthat/test-utils.R
