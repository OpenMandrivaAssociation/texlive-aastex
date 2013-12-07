# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/aastex
# catalog-date 2007-01-26 22:11:52 +0100
# catalog-license lppl
# catalog-version 5.2
Name:		texlive-aastex
Version:	5.2
Release:	6
Summary:	Macros for Manuscript Preparation for AAS Journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aastex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aastex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aastex.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/aastex/aastex.cls
%{_texmfdistdir}/tex/latex/aastex/aastex.sty
%doc %{_texmfdistdir}/doc/latex/aastex/README
%doc %{_texmfdistdir}/doc/latex/aastex/aasclass.tex
%doc %{_texmfdistdir}/doc/latex/aastex/aasguide.pdf
%doc %{_texmfdistdir}/doc/latex/aastex/aasguide.tex
%doc %{_texmfdistdir}/doc/latex/aastex/aassymbols.pdf
%doc %{_texmfdistdir}/doc/latex/aastex/aassymbols.tex
%doc %{_texmfdistdir}/doc/latex/aastex/datafile1.txt
%doc %{_texmfdistdir}/doc/latex/aastex/f1.eps
%doc %{_texmfdistdir}/doc/latex/aastex/f2.eps
%doc %{_texmfdistdir}/doc/latex/aastex/f2_color.eps
%doc %{_texmfdistdir}/doc/latex/aastex/f3.eps
%doc %{_texmfdistdir}/doc/latex/aastex/sample.tex
%doc %{_texmfdistdir}/doc/latex/aastex/table.tex
%doc %{_texmfdistdir}/doc/latex/aastex/video3.mpg

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 5.2-2
+ Revision: 749041
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.2-1
+ Revision: 717781
- texlive-aastex
- texlive-aastex
- texlive-aastex
- texlive-aastex
- texlive-aastex

