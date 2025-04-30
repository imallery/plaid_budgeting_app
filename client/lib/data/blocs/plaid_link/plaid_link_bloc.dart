import 'package:flutter_bloc/flutter_bloc.dart';
import 'plaid_link_event.dart';
import 'plaid_link_state.dart';

class PlaidLinkBloc extends Bloc<PlaidLinkEvent, PlaidLinkState>
{
  PlaidLinkBloc() : super(PlaidLinkLoadingState());



}