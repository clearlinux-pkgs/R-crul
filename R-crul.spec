#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-crul
Version  : 1.2.0
Release  : 37
URL      : https://cran.r-project.org/src/contrib/crul_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/crul_1.2.0.tar.gz
Summary  : HTTP Client
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-curl
Requires: R-httpcode
Requires: R-jsonlite
Requires: R-mime
Requires: R-urltools
BuildRequires : R-R6
BuildRequires : R-curl
BuildRequires : R-httpcode
BuildRequires : R-jsonlite
BuildRequires : R-mime
BuildRequires : R-urltools
BuildRequires : buildreq-R

%description
and mocking HTTP requests. The package is built on R6, and takes

%prep
%setup -q -c -n crul
cd %{_builddir}/crul

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637624653

%install
export SOURCE_DATE_EPOCH=1637624653
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library crul
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library crul
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library crul
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc crul || :


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
/usr/lib64/R/library/crul/doc/best-practices-api-packages.Rmd
/usr/lib64/R/library/crul/doc/best-practices-api-packages.html
/usr/lib64/R/library/crul/doc/choosing-a-client.Rmd
/usr/lib64/R/library/crul/doc/choosing-a-client.html
/usr/lib64/R/library/crul/doc/crul.Rmd
/usr/lib64/R/library/crul/doc/crul.html
/usr/lib64/R/library/crul/doc/curl-options.Rmd
/usr/lib64/R/library/crul/doc/curl-options.html
/usr/lib64/R/library/crul/doc/how-to-use-crul.Rmd
/usr/lib64/R/library/crul/doc/how-to-use-crul.html
/usr/lib64/R/library/crul/doc/index.html
/usr/lib64/R/library/crul/help/AnIndex
/usr/lib64/R/library/crul/help/aliases.rds
/usr/lib64/R/library/crul/help/crul.rdb
/usr/lib64/R/library/crul/help/crul.rdx
/usr/lib64/R/library/crul/help/figures/logo.png
/usr/lib64/R/library/crul/help/paths.rds
/usr/lib64/R/library/crul/html/00Index.html
/usr/lib64/R/library/crul/html/R.css
/usr/lib64/R/library/crul/tests/fixtures/41001c1990.nc
/usr/lib64/R/library/crul/tests/test-all.R
/usr/lib64/R/library/crul/tests/testthat/helper-crul.R
/usr/lib64/R/library/crul/tests/testthat/test-async.R
/usr/lib64/R/library/crul/tests/testthat/test-asyncqueue.R
/usr/lib64/R/library/crul/tests/testthat/test-asyncvaried.R
/usr/lib64/R/library/crul/tests/testthat/test-auth.R
/usr/lib64/R/library/crul/tests/testthat/test-client-delete.R
/usr/lib64/R/library/crul/tests/testthat/test-client-get.R
/usr/lib64/R/library/crul/tests/testthat/test-client-head.R
/usr/lib64/R/library/crul/tests/testthat/test-client-hooks.R
/usr/lib64/R/library/crul/tests/testthat/test-client-patch.R
/usr/lib64/R/library/crul/tests/testthat/test-client-post.R
/usr/lib64/R/library/crul/tests/testthat/test-client-put.R
/usr/lib64/R/library/crul/tests/testthat/test-client-query.R
/usr/lib64/R/library/crul/tests/testthat/test-client-status.R
/usr/lib64/R/library/crul/tests/testthat/test-client-verb.R
/usr/lib64/R/library/crul/tests/testthat/test-client.R
/usr/lib64/R/library/crul/tests/testthat/test-content-type.R
/usr/lib64/R/library/crul/tests/testthat/test-curl_verbose.R
/usr/lib64/R/library/crul/tests/testthat/test-handle.R
/usr/lib64/R/library/crul/tests/testthat/test-head_parse.R
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
