# revision 32003
# category Package
# catalog-ctan /graphics/pgf/contrib/harveyballs
# catalog-date 2013-10-26 15:10:57 +0200
# catalog-license gpl3
# catalog-version 1.1
Name:		texlive-harveyballs
Version:	1.1
Release:	4
Summary:	Create Harvey Balls using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/harveyballs
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harveyballs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harveyballs.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides 5 commands (giving symbols from "none" to
"full").

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/harveyballs/harveyballs.sty
%doc %{_texmfdistdir}/doc/latex/harveyballs/README
%doc %{_texmfdistdir}/doc/latex/harveyballs/harveyballs-Manual.pdf
%doc %{_texmfdistdir}/doc/latex/harveyballs/harveyballs-Manual.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
