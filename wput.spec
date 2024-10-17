%define name	wput
%define version 0.6.1
%define release 3

Name: 		%{name}
Release: 	%{release}
Version: 	%{version}
Summary: 	Uploading files to FTP servers
License: 	GPLv2
Group: 		Networking/File transfer
Source:		http://prdownloads.sourceforge.net/wput/%{name}-%{version}.tar.bz2
URL:		https://wput.sourceforge.net/
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
Wput is the opposite of wget, capable of uploading files to FTP 
servers with an easy to use command line interface similar to 
wget's (old) one.

%prep
%setup -q 
chmod 644 COPYING

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_sysconfdir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 wput %{buildroot}%{_bindir}
install -m 644 doc/wput.1 %{buildroot}%{_mandir}/man1
install -m 644 doc/wputrc %{buildroot}%{_sysconfdir}
(cd po && %makeinstall)
%{find_lang} %{name}

%clean
rm -rf $RPM_BUILS_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog COPYING INSTALL TODO doc
%{_mandir}/man1/wput.1*
%{_bindir}/wput
%config(noreplace) %{_sysconfdir}/wputrc



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-2mdv2011.0
+ Revision: 615462
- the mass rebuild of 2010.1 packages

* Sun Mar 07 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.6.1-1mdv2010.1
+ Revision: 515456
- fix license, source, %%prep
- New version 0.6.1
- use %%configure2_5x

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.6-0.pre.3mdv2010.0
+ Revision: 434981
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.6-0.pre.2mdv2009.0
+ Revision: 140933
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.6-0.pre.2mdv2008.1
+ Revision: 129469
- kill re-definition of %%buildroot on Pixel's request
- import wput


* Thu Apr 20 2006 Lenny Cartier <lenny@mandriva.com> 0.6-0.pre.2mdk
- rebuild for dependencies

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-0.pre.1mdk 
- new version

* Sun Dec 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5-1mdk
- 0.5

* Sun Nov 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.3.4-1mdk
- new
