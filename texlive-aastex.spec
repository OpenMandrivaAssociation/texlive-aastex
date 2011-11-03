# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/aastex
# catalog-date 2007-01-26 22:11:52 +0100
# catalog-license lppl
# catalog-version 5.2
Name:		texlive-aastex
Version:	5.2
Release:	1
Summary:	Macros for Manuscript Preparation for AAS Journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aastex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aastex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aastex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bundle provides a document class for preparing papers for
American Astronomical Society publications. Authors who wish to
submit papers to AAS journals are strongly urged to use this
class in preference to any of the alternatives available.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
