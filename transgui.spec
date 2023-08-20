Summary:	Transmission Remote GUI
Name:		transgui
Version:	5.18.0
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	https://github.com/transmission-remote-gui/transgui/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5c5edc65a7cdec92e25091937b2162a2
URL:		https://github.com/transmission-remote-gui/transgui/
BuildRequires:	lazarus
BuildRequires:	gtk+2-devel
BuildRequires:	pango-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Transmission Remote GUI is feature rich cross platform front-end to
remotely control Transmission daemon via its RPC protocol. It is
faster and has more functionality than builtin Transmission web
interface.

%prep
%setup -q

%build
lazbuild -B "transgui.lpi" --lazarusdir=%{_libdir}/lazarus/
%{__make} OPT="-k--build-id -g -gl -gw -O3"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

cp -a transgui $RPM_BUILD_ROOT%{_bindir}
cp -a lang $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/%{name}
