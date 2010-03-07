%define name	wput
%define version 0.6.1
%define release %mkrel 1

Name: 		%{name}
Release: 	%{release}
Version: 	%{version}
Summary: 	Uploading files to FTP servers
License: 	GPLv2
Group: 		Networking/File transfer
Source:		http://prdownloads.sourceforge.net/wput/%{name}-%{version}.tar.bz2
URL:		http://wput.sourceforge.net/
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

