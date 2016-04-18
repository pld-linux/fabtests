Summary:	Test suite for libfabric API
Summary(pl.UTF-8):	Zestaw testów dla API libfabric
Name:		fabtests
Version:	1.3.0
Release:	1
License:	BSD or GPL v2
Group:		Libraries
#Source0Download: https://github.com/ofiwg/fabtests/releases
Source0:	https://github.com/ofiwg/fabtests/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	2ef01a2bff625b1cf1fcc9891e648866
URL:		https://github.com/ofiwg/fabtests
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.11
BuildRequires:	libfabric-devel >= 1.3.0
BuildRequires:	libtool >= 2:2
BuildRequires:	sed >= 4.0
Requires:	libfabric >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fabtests provides a set of examples that uses libfabric - a
high-performance fabric software library.

%description -l pl.UTF-8
Fabtests to zbiór przykładów wykorzystujących libfabric - bibliotekę
wysoko wydajnych usług sieci typu fabric.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env ruby,/usr/bin/ruby,' scripts/rft_yaml_to_junit_xml

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# don't package plain unit tests
%{__rm} $RPM_BUILD_ROOT%{_bindir}/fi_{av_test,cq_data,dgram*,dom_test,eq_test,msg,msg_epoll,msg_rma,msg_sockets,poll,rdm,rdm_atomic,rdm_rma_*,rdm_multi_recv,rdm_rma,rdm_shared_ctx,rdm_tagged_peek,scalable_ep,size_left_test}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/runfabtests.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING
%attr(755,root,root) %{_bindir}/fi_cmatose
%attr(755,root,root) %{_bindir}/fi_msg_pingpong
%attr(755,root,root) %{_bindir}/fi_rc_pingpong
%attr(755,root,root) %{_bindir}/fi_rdm_cntr_pingpong
%attr(755,root,root) %{_bindir}/fi_rdm_pingpong
%attr(755,root,root) %{_bindir}/fi_rdm_shared_av
%attr(755,root,root) %{_bindir}/fi_rdm_tagged_bw
%attr(755,root,root) %{_bindir}/fi_rdm_tagged_pingpong
%attr(755,root,root) %{_bindir}/fi_ubertest
%attr(755,root,root) %{_bindir}/rft_yaml_to_junit_xml
%{_datadir}/fabtests
%{_mandir}/man7/fabtests.7*
