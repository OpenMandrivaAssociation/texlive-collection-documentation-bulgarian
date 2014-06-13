# revision 19296
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-bulgarian
Epoch:		1
Version:	20120224
Release:	6
Summary:	Bulgarian documentation
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-documentation-bulgarian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-lshort-bulgarian
Requires:	texlive-pst-eucl-translation-bg
Requires:	texlive-collection-documentation-base

%description
TeXLive collection-documentation-bulgarian package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780199
- Update to latest release.
- Import texlive-collection-documentation-bulgarian
- Import texlive-collection-documentation-bulgarian

