#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gss
Version  : 2.1.9
Release  : 8
URL      : https://cran.r-project.org/src/contrib/gss_2.1-9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gss_2.1-9.tar.gz
Summary  : General Smoothing Splines
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-gss-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
function estimation using smoothing splines.

%package lib
Summary: lib components for the R-gss package.
Group: Libraries

%description lib
lib components for the R-gss package.


%prep
%setup -q -c -n gss

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552764915

%install
export SOURCE_DATE_EPOCH=1552764915
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gss
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gss
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gss
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  gss || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gss/CITATION
/usr/lib64/R/library/gss/DESCRIPTION
/usr/lib64/R/library/gss/INDEX
/usr/lib64/R/library/gss/Meta/Rd.rds
/usr/lib64/R/library/gss/Meta/data.rds
/usr/lib64/R/library/gss/Meta/features.rds
/usr/lib64/R/library/gss/Meta/hsearch.rds
/usr/lib64/R/library/gss/Meta/links.rds
/usr/lib64/R/library/gss/Meta/nsInfo.rds
/usr/lib64/R/library/gss/Meta/package.rds
/usr/lib64/R/library/gss/NAMESPACE
/usr/lib64/R/library/gss/R/gss
/usr/lib64/R/library/gss/R/gss.rdb
/usr/lib64/R/library/gss/R/gss.rdx
/usr/lib64/R/library/gss/data/ColoCan.rda
/usr/lib64/R/library/gss/data/LakeAcidity.rda
/usr/lib64/R/library/gss/data/NO2.rda
/usr/lib64/R/library/gss/data/Sachs.rda
/usr/lib64/R/library/gss/data/aids.rda
/usr/lib64/R/library/gss/data/bacteriuria.rda
/usr/lib64/R/library/gss/data/buffalo.rda
/usr/lib64/R/library/gss/data/clim.rda
/usr/lib64/R/library/gss/data/datalist
/usr/lib64/R/library/gss/data/esc.rda
/usr/lib64/R/library/gss/data/eyetrack.rda
/usr/lib64/R/library/gss/data/gastric.rda
/usr/lib64/R/library/gss/data/nox.rda
/usr/lib64/R/library/gss/data/ozone.rda
/usr/lib64/R/library/gss/data/penny.rda
/usr/lib64/R/library/gss/data/stan.rda
/usr/lib64/R/library/gss/data/wesdr.rda
/usr/lib64/R/library/gss/help/AnIndex
/usr/lib64/R/library/gss/help/aliases.rds
/usr/lib64/R/library/gss/help/gss.rdb
/usr/lib64/R/library/gss/help/gss.rdx
/usr/lib64/R/library/gss/help/paths.rds
/usr/lib64/R/library/gss/html/00Index.html
/usr/lib64/R/library/gss/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gss/libs/gss.so
/usr/lib64/R/library/gss/libs/gss.so.avx2
/usr/lib64/R/library/gss/libs/gss.so.avx512
