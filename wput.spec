%define name	wput
%define version 0.6
%define pre	pre
%define release %mkrel 0.%{pre}.2

Name: 		%{name}
Release: 	%{release}
Version: 	%{version}
Summary: 	Uploading files to FTP servers
License: 	GPL
Group: 		Networking/File transfer
Source:		http://prdownloads.sourceforge.net/wput/%{name}-%{pre}%{version}.tar.bz2
URL:		http://wput.sourceforge.net/

%description
Wput is the opposite of wget, capable of uploading files to FTP 
servers with an easy to use command line interface similar to 
wget's (old) one.

%prep
%setup -q -n %{name}
gunzip doc/wput.1.gz
chmod 644 COPYING

%build
%configure
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_sysconfdir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 wput %{buildroot}%{_bindir}
install -m 644 doc/wput.1 %{buildroot}%{_mandir}/man1
install -m 644 doc/wputrc %{buildroot}%{_sysconfdir}
(cd po && %makeinstall)
%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog COPYING INSTALL TODO doc
%{_mandir}/man1/wput.1*
%{_bindir}/wput
%config(noreplace) %{_sysconfdir}/wputrc

