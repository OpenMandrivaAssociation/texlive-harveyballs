%global tl_name harveyballs
%global tl_revision 32003

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Create Harvey Balls using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/harveyballs
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/harveyballs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/harveyballs.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides 5 commands (giving symbols that indicate values
from "none" to "full").

