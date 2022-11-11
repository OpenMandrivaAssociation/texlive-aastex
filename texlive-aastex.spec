Name:		texlive-aastex
Version:	58057
Release:	1
Summary:	Macros for Manuscript Preparation for AAS Journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aastex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aastex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aastex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides a document class for preparing papers for
American Astronomical Society publications. Authors who wish to
submit papers to AAS journals are strongly urged to use this
class in preference to any of the alternatives available.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/aastex
%doc %{_texmfdistdir}/doc/latex/aastex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
